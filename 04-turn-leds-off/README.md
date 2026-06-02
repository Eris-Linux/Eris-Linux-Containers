# Container Example for Eris Linux - Turn LEDS off.

## Description

This project is an example of a container that can be used on the Eris Linux environment.

It turns off all the LEDs of the system.

The container will need `/sys/` access privileges.


This example is very similar to the previous one. However, it is useful for turning off
LEDs that keep flashing even after the previous container has been removed.


## License

This container example is licensed under the MIT license.


## Author

Christophe BLAESS 2026


## Installation

Prepare the container using the  `create-container`  script provided with the Eris Linux containers repository.
For example:

```
$ ./create-container  arm64  ./04-turn-leds-off  turn-leds-off-container
```

After a few minutes, you'll find the container in your build directory:

```
$ ls
  [...]  turn-leds-off-container.tar.bz2 [...]
```

Connect to your account on the [Eris Linux Device Manager](https://www.eris-linux.net).

Go to `My containers` tab and click on the `Upload a container` button to upload your container.
You may enter a password if you want to encrypt the container before it is stored on Eris Linux server.

After container upload, click on the `Setup...` button.
Then fill in the following fields:

- The `Compatible board` field with the type of board on which you'll use the container.
- The `Privileged container` field must be checked in order to access the `/sys/` directory.

Go to `My devices` tab, select the group of devices on which you want to install the container.
On the upper right table, click on the rightmost button of one of the rows (the button with a container icon).
In the list, select your container and click `Ok`.

After a few minutes, when the concerned device will have contacted the Device Manager, downloaded and installed the container, you'll see all the LEDs turn off.

Once the LEDs turned Off, the container will terminate. So it is normal that the slot status appears as `Error` on the device manager.

For more information, see Eris Linux documentation at [www.eris-linux.net](https://www.eris-linux.net).

