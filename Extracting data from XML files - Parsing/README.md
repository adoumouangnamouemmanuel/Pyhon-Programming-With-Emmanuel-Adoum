<h1>Extracting Data from XML</h1>

In this assignment, the program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

<a href="http://py4e-data.dr-chuck.net/comments_42.xml">Sample data</a>: (Sum=2553) <br><br>
<a href="http://py4e-data.dr-chuck.net/comments_1919218.xml">Actual data</a>:  (Sum ends with 95)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

You are to look through all the <strong>comment</strong> tags and find the <strong>count</strong> values sum the numbers.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node