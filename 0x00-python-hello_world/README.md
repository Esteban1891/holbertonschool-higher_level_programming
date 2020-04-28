<div data-role="task1012" data-position="2">
<div id="task-1012" class=" clearfix gap">
<h1 class="gap">0x00. Python - Hello, World</h1>
<h2 class="task">task</h2>
<h4 class="task">1. Run inline&nbsp;mandatory</h4>
<p>Write a Shell script that runs Python code.</p>
<p>The Python code will be saved in the environment variable&nbsp;<code>$PYCODE</code></p>
<pre><code>guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Holberton School: 98
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>1-run_inline</code></li>
</ul>
</div>
</div>
<div data-role="task1013" data-position="3">
<div id="task-1013" class=" clearfix gap">
<h4 class="task">2. Hello, print&nbsp;<span class="alert alert-warning mandatory-optional">mandatory</span></h4>
<p>Write a Python script that prints exactly&nbsp;<code>"Programming is like building a multilingual puzzle</code>, followed by a new line.</p>
<ul>
<li>Use the function&nbsp;<code>print</code></li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
</ul>
</div>
</div>
<div data-role="task1019" data-position="4">
<div id="task-1019" class=" clearfix gap">
<h4 class="task">3. Print integer&nbsp;mandatory</h4>
<p>Complete this&nbsp;<a title="source code" href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" target="_blank">source code</a>&nbsp;in order to print the integer stored in the variable&nbsp;<code>number</code>, followed by&nbsp;<code>Battery street</code>, followed by a new line.</p>
<ul>
<li>You can find the source code&nbsp;<a title="here" href="https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py" target="_blank">here</a></li>
<li>The output of the script should be:
<ul>
<li>the number, followed by&nbsp;<code>Battery street</code>,</li>
<li>followed by a new line</li>
</ul>
</li>
<li>You are not allowed to cast the variable&nbsp;<code>number</code>&nbsp;into a string</li>
<li>Your code must be 3 lines long</li>
<li>You have to use the new print numbers&nbsp;<a title="tips" href="https://intranet.hbtn.io/rltoken/k33L_JH5NMcE3c4LsUkVlA" target="_blank">tips</a>&nbsp;(with&nbsp;<code>.format(...)</code>)</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<blockquote>
<p>C is strongly typed&hellip; not in Python! The variable&nbsp;<code>number</code>&nbsp;can be assigned to a string, a float, a bool etc&hellip; Forcing the type during a string format (<code>"...".format(...)</code>) is a way to control the type of a variable</p>
</blockquote>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>3-print_number.py</code></li>
</ul>
</div>
</div>
<div data-role="task1020" data-position="5">
<div id="task-1020" class=" clearfix gap">
<h4 class="task">4. Print float&nbsp;mandatory</h4>
<p>Complete the source code in order to print the float stored in the variable&nbsp;<code>number</code>&nbsp;with a precision of 2 digits.</p>
<ul>
<li>You can find the source code&nbsp;<a title="here" href="https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py" target="_blank">here</a></li>
<li>The output of the program should be:
<ul>
<li><code>Float:</code>, followed by the float with only 2 digits</li>
<li>followed by a new line</li>
</ul>
</li>
<li>You are not allowed to cast&nbsp;<code>number</code>&nbsp;to string</li>
<li>You have to use the new print formatting&nbsp;<a title="tips" href="https://intranet.hbtn.io/rltoken/CLkyFheLlanPlBS4ySOg7A" target="_blank">tips</a>&nbsp;(with&nbsp;<code>.format(...)</code>)</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>4-print_float.py</code></li>
</ul>
</div>
</div>
<div data-role="task1021" data-position="6">
<div id="task-1021" class=" clearfix gap">
<h4 class="task">5. Print string&nbsp;mandatory</h4>
<p>Complete this&nbsp;<a title="source code" href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" target="_blank">source code</a>&nbsp;in order to print 3 times a string stored in the variable&nbsp;<code>str</code>, followed by its first 9 characters.</p>
<ul>
<li>You can find the source code&nbsp;<a title="here" href="https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py" target="_blank">here</a></li>
<li>The output of the program should be:
<ul>
<li>3 times the value of&nbsp;<code>str</code></li>
<li>followed by a new line</li>
<li>followed by the 9 first characters of&nbsp;<code>str</code></li>
<li>followed by a new line</li>
</ul>
</li>
<li>You are not allowed to use any loops or conditional statement</li>
<li>Your program should be maximum 5 lines long</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>5-print_string.py</code></li>
</ul>
</div>
</div>
<div data-role="task1079" data-position="7">
<div id="task-1079" class=" clearfix gap">
<h4 class="task">6. Play with strings&nbsp;mandatory</h4>
<p>Complete this&nbsp;<a title="source code" href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py" target="_blank">source code</a>&nbsp;to print&nbsp;<code>Welcome to Holberton School!</code></p>
<ul>
<li>You can find the source code&nbsp;<a title="here" href="https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements.</li>
<li>You have to use the variables&nbsp;<code>str1</code>&nbsp;and&nbsp;<code>str2</code>&nbsp;in your new line of code</li>
<li>Your program should be exactly 5 lines long</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>6-concat.py</code></li>
</ul>
</div>
</div>
<div data-role="task1080" data-position="8">
<div id="task-1080" class=" clearfix gap">
<h4 class="task">7. Copy - Cut - Paste&nbsp;mandatory</h4>
<p>Complete this&nbsp;<a title="source code" href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py" target="_blank">source code</a></p>
<ul>
<li>You can find the source code&nbsp;<a title="here" href="https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 8 lines long</li>
<li><code>word_first_3</code>&nbsp;should contain the first 3 letters of the variable&nbsp;<code>word</code></li>
<li><code>word_last_2</code>&nbsp;should contain the last 2 letters of the variable&nbsp;<code>word</code></li>
<li><code>middle_word</code>&nbsp;should contain the value of the variable&nbsp;<code>word</code>&nbsp;without the first and last letters</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>7-edges.py</code></li>
</ul>
</div>
</div>
<div data-role="task1081" data-position="9">
<div id="task-1081" class=" clearfix gap">
<p>Complete this&nbsp;<a title="source code" href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" target="_blank">source code</a>&nbsp;to print&nbsp;<code>object-oriented programming with Python</code>, followed by a new line.</p>
<ul>
<li>You can find the source code&nbsp;<a title="here" href="https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 5 lines long</li>
<li>You are not allowed to create new variables</li>
<li>You are not allowed to use string literals</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
</ul>
</div>
</div>
<div data-role="task1082" data-position="10">
<div id="task-1082" class=" clearfix gap">
<p>Write a Python script that prints &ldquo;The Zen of Python&rdquo;, by TimPeters, followed by a new line.</p>
<ul>
<li>Your script should be maximum 98 characters long (please check with&nbsp;<code>wc -m 9-easter_egg.py</code>)</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>9-easter_egg.py</code>10. Linked list cycle&nbsp;<span style="font-size: 1em;">mandatory</span></li>
</ul>
</div>
</div>
<div data-role="task2656" data-position="11">
<div id="task-2656" class=" clearfix gap">
<p><strong>Technical interview preparation</strong>:</p>
<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
<li>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution&rsquo;s runtime fast enough, does your solution require extra memory usage / mallocs, etc.</li>
</ul>
<p>Write a function in C that checks if a singly linked list has a cycle in it.</p>
<ul>
<li>Prototype:&nbsp;<code>int check_cycle(listint_t *list);</code></li>
<li>Return:&nbsp;<code>0</code>&nbsp;if there is no cycle,&nbsp;<code>1</code>&nbsp;if there is a cycle</li>
</ul>
<p>Requirements:</p>
<ul>
<li>Only these functions are allowed:&nbsp;<code>write</code>,&nbsp;<code>printf</code>,&nbsp;<code>putchar</code>,&nbsp;<code>puts</code>,&nbsp;<code>malloc</code>,&nbsp;<code>free</code></li>
</ul>
<pre><code>carrie@ubuntu:~/0x00$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include &lt;stdlib.h&gt;

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
</code></pre>
<pre><code>carrie@ubuntu:~/0x00$ cat 10-linked_lists.c
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current-&gt;n);
        current = current-&gt;next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new-&gt;n = n;
    new-&gt;next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head-&gt;next;
        free(current);
    }
}
</code></pre>
<pre><code>carrie@ubuntu:~/0x00$ cat 10-main.c
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&amp;head, 0);
    add_nodeint(&amp;head, 1);
    add_nodeint(&amp;head, 2);
    add_nodeint(&amp;head, 3);
    add_nodeint(&amp;head, 4);
    add_nodeint(&amp;head, 98);
    add_nodeint(&amp;head, 402);
    add_nodeint(&amp;head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i &lt; 4; i++)
        current = current-&gt;next;
    temp = current-&gt;next;
    current-&gt;next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i &lt; 4; i++)
        current = current-&gt;next;
    current-&gt;next = temp;

    free_listint(head);

    return (0);
}
</code></pre>
<pre><code>carrie@ubuntu:~/0x00$ gcc -Wall -Werror -Wextra -pedantic 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
carrie@ubuntu:~/0x00$$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
carrie@ubuntu:~/0x00$
</code></pre>
<blockquote>
<p>Solving a problem is already a big win! but finding the best and optimal way to solve it, it&rsquo;s way better! Think about the most optimal / fastest way to do it.</p>
</blockquote>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>10-check_cycle.c, lists.h</code></li>
</ul>
</div>
</div>
<div data-role="task1014" data-position="100">
<div id="task-1014" class=" clearfix gap">
<h4 class="task">11. Hello, write&nbsp;<span class="alert alert-info mandatory-optional">#advanced</span></h4>
<p>Write a Python script that prints exactly&nbsp;<code>and that piece of art is useful - Dora Korpar, 2015-10-19</code>, followed by a new line.</p>
<ul>
<li>Use the function&nbsp;<code>write</code>&nbsp;from the&nbsp;<code>sys</code>&nbsp;module</li>
<li>You are not allowed to use&nbsp;<code>print</code></li>
<li>Your script should print to&nbsp;<code>stderr</code></li>
<li>Your script should exit with the status code&nbsp;<code>1</code></li>
<li>(Dora Korpar was a Holberton student in Cohort 0 of San Francisco)</li>
</ul>
<pre><code>guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2&gt; q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li></li>
</ul>
</div>
</div>
<div data-role="task1010" data-position="101">
<div id="task-1010" class=" clearfix gap">
<p>Write a script that compiles a Python script file.</p>
<p>The Python file name will be stored in the environment variable&nbsp;<code>$PYFILE</code></p>
<p>The output filename has to be&nbsp;<code>$PYFILEc</code>&nbsp;(ex:&nbsp;<code>export PYFILE=my_main.py</code>&nbsp;=&gt; output filename:&nbsp;<code>my_main.pyc</code>)</p>
<pre><code>guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./101-compile
Compiling main.py ...
guillaume@ubuntu:~/py/0x00$ ls
101-compile  main.py  main.pyc
guillaume@ubuntu:~/py/0x00$ cat main.pyc | zgrep -c "Holberton School"
1
guillaume@ubuntu:~/py/0x00$ od -t x1 main.pyc # SYSTEM DEPENDANT =&gt; CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
 
</code></pre>
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository:&nbsp;<code>holbertonschool-higher_level_programming</code></li>
<li>Directory:&nbsp;<code>0x00-python-hello_world</code></li>
<li>File:&nbsp;<code>101-compile</code></li>
</ul>
</div>
</div>
<div data-role="task1025" data-position="102">
<div id="task-1025" class=" clearfix gap">
<h4 class="task">13. ByteCode -&gt; Python #1</h4>
</div>
</div>
