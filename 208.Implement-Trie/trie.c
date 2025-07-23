#include <stdlib.h>
#include <stdbool.h>

#define CHILDREN_LEN 26
#define CAP ('a' + 26)
#define nth_child(t, i) (t)->children[(i) - 'a']

typedef struct Trie {
    struct Trie *children[CHILDREN_LEN];
    size_t count;
    bool end;
} Trie;


static inline bool
contains_symbol(Trie *t, char symbol)
{
    return nth_child(t, symbol) != NULL;
}


static inline bool
str_is_empty(char *str)
{
    return *str == '\0';
}


static inline bool
str_is_last_char(char *str)
{
    return str_is_empty(str + 1);
}


Trie *
trieCreate()
{
    return calloc(1, sizeof(Trie));
}


void
__trieInsert(Trie *t, char *str)
{
    if (str_is_empty(str)) {
        return;
    }

    if (!contains_symbol(t, *str)) {
        Trie *symbol = trieCreate();
        nth_child(t, *str) = symbol;
        t->count++;

        if (str_is_last_char(str)) {
            symbol->end = true;
            return;
        }

    } else if (str_is_last_char(str)) {
        nth_child(t, *str)->end = true;
        return;
    }

    __trieInsert(nth_child(t, *str), str + 1);
}


void
trieInsert(Trie *t, char *str)
{
    if (!t) return;

    if (str_is_empty(str)) {
        bool prev = t->end;
        t->end = true;
    } else {
        __trieInsert(t, str);
    }
}


static bool
__trieSearch(Trie *t, char *str)
{
    if (str_is_empty(str)) {
        return false;
    }

    if (!contains_symbol(t, *str)) {
        return false;
    }

    if (nth_child(t, *str)->end && str_is_last_char(str)) {
        return true;
    }

    return __trieSearch(nth_child(t, *str), str + 1);
}


bool
trieSearch(Trie *t, char *str)
{
    if (!t) return false;
    return __trieSearch(t, str);
}


bool
__trieStartsWith(Trie *t, char *prefix)
{
    if (str_is_empty(prefix)) {
        return true;
    }

    if (!contains_symbol(t, *prefix)) {
        return false;
    }

    return __trieStartsWith(nth_child(t, *prefix), prefix + 1);
}


bool
trieStartsWith(Trie *t, char *prefix)
{
    if (!t) return false;
    return __trieStartsWith(t, prefix);
}


void
trieFree(Trie* t)
{
    if (!t) return;

    for (int i = 'a'; i < CAP; i++) {
        if (t->count == 0) break;

        if (nth_child(t, i)) {
            trieFree(nth_child(t, i));
            t->count--;
        }
    }

    free(t);
}
