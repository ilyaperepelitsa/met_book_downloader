# MET museum book downloader
### Downloads ONLY PDF books posted on
[MET Website](https://www.metmuseum.org/art/metpublications/all-available-titles)
### Original [post](https://news.ycombinator.com/item?id=16303046)
### from [YC News aka. HackerNews](https://news.ycombinator.com)

In order to install scrapy do the following:

```
pip3 install scrapy
pip3 install scrapy-fake-useragent
```
or if your default python is python 3:
```
pip install scrapy
pip install scrapy-fake-useragent
```

Then go select a directory and do the following in the terminal:

```
cd Users/parent_folder
git clone https://github.com/ilyaperepelitsa/met_book_downloader   
cd met_book_downloader
```

And run scrapy. It will create a folder called **full** in repository
folder and save all the files there. Make sure you have enough space
since the files are bulky (art books containing images).

```
scrapy crawl met
```

The **settings** file in the FERC directory has the setting:
``` python
DOWNLOAD_DELAY = 10
```
This means that requests would be delayed by 10 seconds - doing that to be gentle wit
[MET](https://www.metmuseum.org/art/metpublications/all-available-titles) servers. Please
Either run this scraper late 

Known issues (checked manually)
Books not downloaded properly due to size - can't check right now, website is slow
(added the setting that wouldn't glitch out on large files, should work in theory)
Books not downloaded properly due to Met's file address redirecting to ".pdf.html"
