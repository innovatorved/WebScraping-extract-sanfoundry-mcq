
# WebScraping project-extract-sanfoundry-mcq

Web Scrapping Project extract MCQ of any topic from sanfoundry.com in pdf form

## Run Locally

Create Directory

```bash
mkdir ProjectWebScrapper
cd ProjectWebScrapper
```

Clone the project

```bash
  git clone https://github.com/innovatorved/WebScraping-extract-sanfoundry-mcq.git .
```

Import Class and use

```bash
  cd ProjectWebScrapper
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Import Class And Use

```python

    # Import Class
    from sanfoundryClass import copyit

    # Change the link
    url = "https://www.sanfoundry.com/operating-system-questions-answers-basics/"
    data = copyit(url)

    print(data.copyright())

    # print(len(data.extract_list()))
    # print(len(data.extract_dict()))
    # print(data.extract_str()[:100])

    # PDF save as title Name
    data.extract_pdf()
```

  
## Acknowledgements

 - [Start with Python](https://github.com/innovatorved/BasicPython)
 - [Python recall for Developers](https://github.com/innovatorved/python-recall)
 - [Comptetive Programing with C++](https://github.com/innovatorved/Comptetive-Programing-cpp)

  
## Authors

- [@Ved Gupta](https://github.com/innovatorved)

  
## Feedback

If you have any feedback, please reach out to us at vedgupta@protonmail.com