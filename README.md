# PolyCTF

## About
A competition aimed to draw talented students into the lab as well as make everyone at Poly aware that the lab actually exists

## Challenge Areas
* Cryptography
* Binary Exploitation
* Forensics
* Programming
* Recon
* Reversing
* Web Exploitation

## Challenge Ideas
* Introduction
    - [x] nc
    * linux
        - [ ] cd, grep, find, strings, cat -> pipe, env vars
        - [ ] cat <file> - | ./<prog> (keep stdin open)
    - [x] base64
    - [x] Ceasar
    - [x] Hashing
    - [ ] Git
    - [ ] Javascript Console / View Source
    - [x] Filter out non alpha-numeric characters
    - [x] Strings on a file
    - [ ] Connect to IRC

* Binary Exploitation
    - [x] Integer Overflow
    * Sandboxes
        - [ ] Shellcode
        - [ ] Python
    * Buffer Overflow
        - [x] Change stack variable
    * ROP
        - [x] Change return address
        - [x] Go into shellcode
        - [x] Ret-to-libc
    * Format String
        - [ ] Change global variable
        - [ ] Change got addr w/ leak
        - [ ] Change got addr w/o leak
    - [ ] Stack Canary (PicoCTF)
    * Heap
        - [ ] Heap Overflow
        - [ ] Use after free

* Web Exploitation
    - [ ] Page Source (look at page source)
    - [x] Heartbleed thing
    * SQL Injection
        - [ ] Login with SQL injection
        - [ ] Null Selection (leak out db info)
        - [ ] Like Query (brute out password)
    * XSS
        - [ ] Alert on page
        v JS Bot (Make bot run js)
    - [ ] Alchemy (exploit bug to win game)

* Forensics
    - [ ] Modify GBA Rom
    - [ ] Packet Capture Pokemon between two GBAs
    - [ ] ZIP Bomb (small)
    - [ ] Image Size in Metadata
    - [ ] Carving
    * PCAP
        - [ ] Telnet
        - [x] ICMP Ping with Data
        - [ ] Encrypted Traffic (Superfish Cert)
    - [ ] Steg?
    - [ ] Memory Dump Analysis
    - [ ] Lots of images find different time stamps
    - [ ] Shuffle JPEG blocks, keep CRC hashes in right place
    - [X] Image Mounting / Disk Forensics 
    - [ ] Memory analysis

* Crypto
    * [x] Math formula thing
    * RSA Formula
        - [x] All factors given
        - [ ] Factors missing
    - [ ] Hash Extension
    * XOR Breaking
        - [x] Single Key
        - [x] Multiple Character Key
    - [ ] Hash Collision
    * _Crypto Pals for ideas_

* Misc.
    - [ ] Guess movie from hack scene (computer ui)
    - [ ] X-Y-Z
    - [ ] Konami Code on Site
    - [ ] Ed, the standard editor

* Reverse Engineering
    - [ ] ARM
    - [ ] .NET
    - [ ] Esoteric Languages
    - [ ] Calculate code coverage to get pass (Pin)
    - [ ] Slow Pong (Speed Hack)
    * RPI Bomb Parts
        - [x] Single Character Comparision in Pass
        - [x] Follow Graph Data Structure
        - [x] Seed Function with Random Output
    - [ ] APK

* Web Exploitation
    - [ ] Alert something on the page
    - [ ] Javascript bot on server side evaluating what is sent
    - [ ] Execute javascript in console
    - [ ] Robots.txt
    - [ ] Race condition
    - [ ] Headers

* Scripting
    * Game solving
        - [ ] Tic Tack Toe
        - [ ] Maze Oracle
        - [ ] Rock Paper Scissor
    - [ ] Password Compare Timing Attack
    - [ ] Bank Fractions of a Penny
    - [ ] Recruit QR
    - [ ] JSON Linked List of Links
    - [ ] Determine next digits of PI
    - [ ] Wikipedia Game

* Recon
    - [ ] Game Lab Stream Key
    * Get into places
        - [ ] The Art
        - [ ] ISIS Lab
        - [ ] Othmer
        - [ ] Clark
        - [ ] Ontop of Rogers
    - [ ] Give us an online account
    - [ ] Solve 2048
    - [ ] Given starting location and velocity graph determine destition
    - [ ] Get letter paper
    - [ ] Break WEP
    - [ ] By Particular Objects from Lackman
    - [ ] Determine someone's favorite resturant

## Tools
* Ubuntu Download
* VMware Site / Virtual Box
* IDA / Hopper / Binja
*
