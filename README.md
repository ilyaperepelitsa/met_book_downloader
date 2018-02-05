#MET museum book downloader
### Downloads ONLY PDF books posted on
[MET Website](https://www.metmuseum.org/art/metpublications/all-available-titles)
### Original [post](https://news.ycombinator.com/item?id=16303046)
###from [YC News aka. HackerNews](https://news.ycombinator.com)

In order to install scrapy do the following:

```
pip3 install scrapy
```
or if your default python is python 3:
```
pip install scrapy
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

Known issues (checked manually)
Books not downloaded properly due to size
* 2 GB [Art of Medieval Spain](http://resources.metmuseum.org/resources/metpublications/pdf/The_Art_of_Medieval_Spain_AD_500_1200.pdf)
* 200 MB [American Stories Paintings of everyday life](http://resources.metmuseum.org/resources/metpublications/pdf/American_Stories_Paintings_of_Everyday_Life_1765_1915.pdf)
* 200 MB [Art of Illumination](http://resources.metmuseum.org/resources/metpublications/pdf/The_Art_of_Illumination_The_Limbourg_Brothers_and_the_Belles_Heures_of_Jean_de_France_Duc_de_Berr.pdf)


Books not downloaded properly due to Met's file address redirecting to ".pdf.html"
(Don't want to troubleshoot HTTP requests tbh, easier to look by name at [MET Website](https://www.metmuseum.org/art/metpublications/all-available-titles))

* [Artistic furniture of the Gilded Age](http://resources.metmuseum.org/resources/metpublications/pdf/Artistic_Furniture_of_the_Gilded_Age.pdf)
