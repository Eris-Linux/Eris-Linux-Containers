# Container Example for Eris Linux - HTTPS Hello World in Python

## Description

This project is an example of a container that can be used on the Eris Linux environment.

The application provides an HTTPS server on port 443 of the container, which displays "Hello World".

The application is written in Python.



## License

This container example is licensed under the MIT license.


## Author

ChatGPT 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers package.
For example:

```
$ ./create-container  arm64  ./11-hello-world-in-python  hello-world-in-python
```

After a few minutes, you'll find the container image in your build directory:

```
$ ls
  [...]  hello-world-in-python   [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.
- The `Exported Ports` field with `443:443/tcp`.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, you can reach the application
using a web browser at the URL: `https://<device-ip-address>`

The browser will warn you about security. It's normal, the HTTPS server provides an autosigned certificate.


For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

