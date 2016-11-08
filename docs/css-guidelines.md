#CSS guidelines for developers

This document is explains the rulesets used for frontend development at Opin.me. 

##Coding style

Since we are using bootstrap, we found it convenient to try and adapt their coding style
as much as possible. The guide can be found on http://codeguide.co/.

We did make one small deviation from the codeguide and decided to use four spaces instead
of two. 
You are encouraged to follow these rulesets to ensure a quick merge of your pull-
request.

To furthermore make sure, these guidelines are followed, we use http://stylelint.io/. The rules specified
in the .stylelintrc.json file will be checked against the entire SCSS code before allowing a commit.

##Class names

The conventions for class names are an extended version of the ones you can find on codeguide.co:

* no underscores, all lowercase
* the first word in a class will always be the container of a component (this also goes for dash-
  separated words, they will be written together as one word) 
  `.btn`
* if the component has a child element, the relation will be emphasized with a dash between container
  and child element 
  `.tweet-header`
* should a class modify the usual appearance of an element, it will follow a dash as well
  `.btn-danger`
* use dashes only to emphasize a child-parent relation or a modifier 
  `.dropdown-large` instead of `.drop-down-large` 
  and `.tweetbox-title` instead of `.tweet-box-title` 
  
###Examples:

####Button:
  ```
  <button class="btn btn-danger">Hello World</button>
                  |         |
              base class    |
                      modifier class
  ```
  
  
####Tweet element:
  ```
                child-element class
            base class  |
                |       |      child-element modifier class
  <div class="tweet">   |            |
      <div class="tweet-header tweet-header-large">
          <h3 class="tweet-title">Hello World</h3>
      </div>
      <div class="tweet-body">
          Lorem ipsum dolor sit amet.
      </div>
  </div>
  ```
