use std::collections::{BinaryHeap, HashMap, HashSet};

type Tweet = i32;

#[derive(Default)]
struct User {
    followee: HashSet<i32>,
    tweets: Vec<(usize, Tweet)>,
}

#[derive(Default)]
struct Twitter {
    users: HashMap<i32, User>,
    n_tweets: usize,
}

const FEED_COUNT: usize = 10;

impl Twitter {
    fn new() -> Self {
        Self::default()
    }

    fn post_tweet(&mut self, user_id: i32, tweet: Tweet) {
        let user = self.users.entry(user_id).or_default();

        user.tweets.push((self.n_tweets, tweet));
        self.n_tweets += 1;
    }

    fn get_news_feed(&self, user_id: i32) -> Vec<Tweet> {
        let Some(user) = self.users.get(&user_id) else {
            return Vec::new();
        };

        // O(n + N)
        let heap: BinaryHeap<_> = user
            .followee
            .iter()
            // Get followee's tweets.
            .map(|f| self.users.get(f).map(|u| u.tweets.iter()))
            .flatten()
            .flatten()
            // Chain own tweets.
            .chain(user.tweets.iter())
            .collect();

        // O(log(n + N))
        (0..10)
            .scan(heap, |h, _| h.pop().map(|&(_, id)| id))
            .collect()
    }

    fn follow(&mut self, user_id: i32, follower_id: i32) {
        let user = self.users.entry(user_id).or_default();
        user.followee.insert(follower_id);
    }

    fn unfollow(&mut self, user_id: i32, unfollower_id: i32) {
        if let Some(user) = self.users.get_mut(&user_id) {
            user.followee.remove(&unfollower_id);
        }
    }
}
