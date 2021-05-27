# Spam recognizer

It's a simple application that uses machine learning to classify spam. To run it you have to have [Docker](https://docs.docker.com/get-docker/) installed.

To start the application navigate to directory containing Dockerfile and run the following commands using Terminal (Linux) or CMD(Windows):

1. `docker build . -t spam-recognizer`
2. `docker run -it --rm spam-recognizer`

While inside the application, type any text and press `ENTER` to check whether it's spam or ham.
To exit, type `exit()` and press `ENTER`.

Authors:

- [Dominik Bilski](https://github.com/Kinimod12)
- [Wojciech Dębski](https://github.com/wdebsqi)
