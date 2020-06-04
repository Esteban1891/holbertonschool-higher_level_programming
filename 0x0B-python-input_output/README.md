<h1>0x0B. Python - Input/Output</h1>
<h2><a id="user-content-resourcesbooks" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#resourcesbooks"></a>Resources📚</h2>
<p>Read or watch:</p>
<ul>
<li><a href="https://intranet.hbtn.io/rltoken/c5ypFfQwcM-SZ-7tr3WuxA" rel="nofollow">7.2. Reading and Writing Files</a></li>
<li><a href="https://intranet.hbtn.io/rltoken/1wqMFejKqBva-Lxws0lftw" rel="nofollow">8.7. Predefined Clean-up Actions</a></li>
<li><a href="https://intranet.hbtn.io/rltoken/8aSPOpBZj9B1DB6GfoEWfg" rel="nofollow">Dive Into Python 3: Chapter 11. Files</a></li>
<li><a href="https://intranet.hbtn.io/rltoken/XBqM3BrA_rUBw6DXw4X98Q" rel="nofollow">JSON encoder and decoder</a></li>
<li><a href="https://intranet.hbtn.io/rltoken/derf9VLFVDnSgX2n-drwnw" rel="nofollow">Learn to Program 8 : Reading / Writing Files</a></li>
<li><a href="https://intranet.hbtn.io/rltoken/Y77h8aeRoljlN643yKfdTg" rel="nofollow">Automate the Boring Stuff with Python</a></li>
</ul>
<hr />
<h2><a id="user-content-learning-objectivesbulb" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#learning-objectivesbulb"></a>Learning Objectives💡</h2>
<p>What you should learn from this project:</p>
<ul>
<li>Why Python programming is awesome (don&rsquo;t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>How to open a file</li>
<li>How to write text in a file</li>
<li>How to read the full content of a file</li>
<li>How to read a file line by line</li>
<li>How to move the cursor in a file</li>
<li>How to make sure a file is closed after using it</li>
<li>What is and how to use the with statement</li>
<li>What is JSON</li>
<li>What is serialization</li>
<li>What is deserialization</li>
<li>How to convert a Python data structure to a JSON string</li>
<li>How to convert a JSON string to a Python data structure</li>
</ul>
<hr />
<h3><a id="user-content-0-read-file" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#0-read-file"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/0-read_file.py">0. Read file</a></h3>
<ul>
<li>Write a function that reads a text file (UTF8) and prints it to stdout:</li>
</ul>
<h3><a id="user-content-1-number-of-lines" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#1-number-of-lines"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/1-number_of_lines.py">1. Number of lines</a></h3>
<ul>
<li>Write a function that returns the number of lines of a text file:</li>
</ul>
<h3><a id="user-content-2-read-n-lines" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#2-read-n-lines"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/2-read_lines.py">2. Read n lines</a></h3>
<ul>
<li>Write a function that reads n lines of a text file (UTF8) and prints it to stdout:</li>
</ul>
<h3><a id="user-content-3-write-to-a-file" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#3-write-to-a-file"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/3-write_file.py">3. Write to a file</a></h3>
<ul>
<li>Write a function that writes a string to a text file (UTF8) and returns the number of characters written:</li>
</ul>
<h3><a id="user-content-4-append-to-a-file" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#4-append-to-a-file"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/4-append_write.py">4. Append to a file</a></h3>
<ul>
<li>Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:</li>
</ul>
<h3><a id="user-content-5-to-json-string" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#5-to-json-string"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/5-to_json_string.py">5. To JSON string</a></h3>
<ul>
<li>Write a function that returns the JSON representation of an object (string):</li>
</ul>
<h3><a id="user-content-6-from-json-string-to-object" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#6-from-json-string-to-object"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/6-from_json_string.py">6. From JSON string to Object</a></h3>
<ul>
<li>Write a function that returns an object (Python data structure) represented by a JSON string:</li>
</ul>
<h3><a id="user-content-7-save-object-to-a-file" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#7-save-object-to-a-file"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/7-save_to_json_file.py">7. Save Object to a file</a></h3>
<ul>
<li>Write a function that writes an Object to a text file, using a JSON representation:</li>
</ul>
<h3><a id="user-content-8-create-object-from-a-json-file" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#8-create-object-from-a-json-file"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/8-load_from_json_file.py">8. Create object from a JSON file</a></h3>
<ul>
<li>Write a function that creates an Object from a &ldquo;JSON file&rdquo;:</li>
</ul>
<h3><a id="user-content-9-load-add-save" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#9-load-add-save"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/9-add_item.py">9. Load, add, save</a></h3>
<ul>
<li>Write a script that adds all arguments to a Python list, and then save them to a file:</li>
</ul>
<h3><a id="user-content-10-class-to-json" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#10-class-to-json"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/10-class_to_json.py">10. Class to JSON</a></h3>
<ul>
<li>Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:</li>
</ul>
<h3><a id="user-content-11-student-to-json" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#11-student-to-json"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/11-student.py">11. Student to JSON</a></h3>
<ul>
<li>Write a class Student that defines a student by:</li>
</ul>
<h3><a id="user-content-12-student-to-json-with-filter" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#12-student-to-json-with-filter"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/12-student.py">12. Student to JSON with filter</a></h3>
<ul>
<li>Write a class Student that defines a student by: (based on 11-student.py)</li>
</ul>
<h3><a id="user-content-13-student-to-disk-and-reload" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#13-student-to-disk-and-reload"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/13-student.py">13. Student to disk and reload</a></h3>
<ul>
<li>Write a class Student that defines a student by: (based on 12-student.py)</li>
</ul>
<h3><a id="user-content-14-pascals-triangle" class="anchor" href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/tree/master/0x0B-python-input_output#14-pascals-triangle"></a><a href="https://github.com/Esteban1891/holbertonschool-higher_level_programming/blob/master/0x0B-python-input_output/14-pascal_triangle.py">14. Pascal's Triangle</a></h3>
<ul>
<li>Technical interview preparation:</li>
<li></li>
</ul>
