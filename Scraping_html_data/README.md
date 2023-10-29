<h1>Web Scraping</h1>
<h2> 1 - Scraping Numbers from HTML using BeautifulSoup</h2> 

In this assignment the program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

<a href="http://py4e-data.dr-chuck.net/comments_42.html">Sample data</a>:  (Sum=2553) <br>
<a href='http://py4e-data.dr-chuck.net/comments_1919216.html'>Actual data</a>:  (Sum ends with 5)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. <br>

<h3>Data Format</h3>
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

You are to find all the "span" tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.

<h2> 2 - Following Links in Python</h2>

In this assignment, the program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah <br><br>
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Siobhan.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.

<h3>Hint</h3>: The first character of the name of the last page that you will load is: <strong>P</strong>

<h3>Strategy</h3>
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.