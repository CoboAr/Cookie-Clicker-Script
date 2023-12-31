# Cookie Clicker Game Script

## Requirements
pip install Selenium       
pip install --upgrade pip

## What is Cookie Clicker Script?
It is a python bot created with Selenium that is going to play the addictive Cookie Clicker game: https://orteil.dashnet.org/cookieclicker/  automatically.
The basic idea of Cookie Clicker game is a giant cookie that the user needs to click on it as fast as he can where each click generates a cookie. Once the user has enough cookies, he can purchase certain product and upgrades like:
<ol>
  <li>A cursor that clicks on the cookie automatically for the user.</li>
  <li>A gradma that bakes more cookies for the user.</li>
</ol>

Cookie Clicker bot is going to decide which products to buy that makes sense, and click on the giant cookie to bake even more cookies. The more of the products and upgrades the user buys, tge more often the users clicks on the giant cookie, the more cookies per second the user can bake. The goal is not to touch mouse and use Selenium to play this game and generate a high score (Cookies per second) in 5 minutes.   

https://github.com/CoboAr/Cookie-Clicker-Script/assets/144629565/f441e660-32d7-476d-a9ca-ac47e6f43f7e

## How does it work?

Once the script is running:

<ol>
  <li>
    It clicks on the cookie as fast as possible.
  </li>
  <li>
    Every 11.2 seconds, it checks the right-hand pane to see which products are affordable and purchase the most expensive one.
  </li>
  <li>
    Every 18 seconds, it checks the right-hand pane to see which upgrades are affordable and purchase the first one on the list.
  </li>
  <li>
    After 5 minutes have passed since starting the game, the bot will stop and print the "cookies/second" score.
  </li>
</ol>

## Demo

https://github.com/CoboAr/Cookie-Clicker-Script/assets/144629565/6eda8ac1-c7ca-4786-b640-eee0f9458295

<img width="1440" alt="Screenshot 2023-12-30 at 9 41 39 PM" src="https://github.com/CoboAr/Cookie-Clicker-Script/assets/144629565/e9459166-cf6d-4985-9c19-570c5bbf18d7">

The game might be updated and the source code might change in the future. In this event, Cookie Clicker Game Script might not be functional.   

Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo




