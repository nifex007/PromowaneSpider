# PromowaneSpider

## The web crawling task for Python developer will be:
- Go to olx.pl page.
- Get list of "Ogłoszenia promowane" - promoted advertisements.
- Get every item's title, price(as number), description(in html) and image url
- Save list to json file with provided format:

```
[
  {
    "title": "...",
    "description": "...",
    "price": 200.95,
    "image": "https://..."
  },
  {...}
] 
```

 ### Setup

 ```
  $ make setup
 ```

 ### Run

 ```
 $ cd PromowaneSpider
 $ make run
 ```

 `output.json ` should be populated with the list "Ogłoszenia promowane" - promoted advertisements


 ### TODO 

 - Logging 
 - Automated Tests 





