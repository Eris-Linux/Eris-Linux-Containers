# Sample code for Eris Linux

## Description

The code in this directory is destinated for testing the debug mode of Eris Linux.


## License

This sample container is licensed under the MIT license.


## Author

Christophe Blaess 2026.

## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers package.
For example:

```
$ ./create-container  arm64  ./test-debug-stdio  test-debug-stdio
```

After a few seconds, you'll find the container image in your build directory:

```
$ ls
  [...]  test-debug-stdio   [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

To use the Eris Linux debug methods, please follow the instructions described in this article (in french):

https://www.blaess.fr/christophe/2026/10/07/debug-applicatif-avec-eris-linux/


For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

