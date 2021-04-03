# Create braille data
The idea is compare the braille dots as a matrix and each element as a bit
```
⡏b1 b2⢹
⡇b3 b4⢸ 
⡇b5 b6⢸ ---> 2⁸*b8 + 2⁷*b7 + ... + 2*b2 + 1* b1
⣇b7 b8⣸
 
 ```
 and store each bit in a integer.
