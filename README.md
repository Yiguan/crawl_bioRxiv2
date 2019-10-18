# crawl_bioRxiv2

Summarise the number of word in each section of submitted articles on bioRxiv.

After data cleaning, a total of 42,348 submitted papers on bioRxiv were analyzed here (before Oct 15, 2019). 

### Summary of word count in each section 

1. ABSTRACT

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/abstract.png)

[Bule vertical dashed lines indicate integer numbers from 150 to 400 with step = 50. Clear peaks were showed in these vertical lines.]

* It seems many authors were trying to delete some words to meet the criteria of journals before submitted.*

2. INTRODUCTION

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/introduction.png)

3. METHOD

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/method.png)

4. RESULT

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/result.png)

5. DISCUSSION

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/discussion.png)

6. Number of REFERENCE

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/reference.png)

7. Put all section together

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/all.png)

[x-aixs was truncated at 50000]

### Correlation among each section

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/corr.png)

### Relationship between REFERENCE and each section

![](https://github.com/Yiguan/crawl_bioRxiv2/blob/master/glm.png)

Using mutilple linear regression, all sections expect ABSTRACT had impacts on the number of REFERENCE.As expected, the length of DISCUSSION has the largest impact on the number of REFERENCE.

### DATA

<https://github.com/Yiguan/crawl_bioRxiv2/blob/master/bioData_clean.txt>
