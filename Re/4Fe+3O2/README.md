# 4Fe+3O2

Reversing a Rust binary with debug symbols enabled

Creator - [@PlatyPew](https://github.com/PlatyPew)

## Category

Reverse Engineering

## Question

> Rust is really versatile. First, you can write systems programming with Rust and suddenly realise it's not as scary, or have Rust’s compiler flashing those friendly error messages, or have Rust stealing the bugs from your code and putting them on like, "Haha, fixed your bugs!" That's just way too cool! Also, Rust's ownership model! I really like when it enforces memory safety with that reassuring borrow checker gleam, and it's amazing how it can look really powerful or just be a learning aid. I really like how it can fulfil all those abstract coding needs. Being able to switch up the patterns and abstractions based on your project is a lot of fun too! It's actually so much fun! You have those zero-cost abstractions, or the fearless concurrency, everything! It's like you're enjoying all these kinds of features at a buffet. I really want more developers to try it out or replace their old tools with Rust. We really need Rust to become a thing in more codebases and start seeing it everywhere. Don't. You. Think. We. Really. Need. To. Officially. Embrace. Rust?
>
> Connect via `nc <ip address> 30001`

### Hint

- First step seems to be a simple comparison
- What is this magic function? It looks recursive.
- There seems to be 2 functions named `ironoxide::levelthree`

## Setup Guide

`docker compose up -d ironoxide`

## Distribution

- ironoxide: `0047d6e9fd94ad4d14337735066a8161f455facc32a6503767aadf5e5bb64bfa`

## Solution

Use a decompiler like IDA to decompile `ironoxide::main()`.
We can see there are 3 levels to clear.

```c
__int64 ironoxide::main()
{
  __int64 result; // x0
  __int64 flag; // x0
  __int64 v2; // x0

  result = ironoxide::level_one();
  if ( (result & 1) != 0 ) {
    flag = ironoxide::get_flag(&aFlag1Txt, 11LL);
    result = ironoxide::level_two(flag);
    if ( (result & 1) != 0 )
    {
      v2 = ironoxide::get_flag(&aFlag2Txt, 11LL);
      result = ironoxide::level_three(v2);
      if ( (result & 1) != 0 )
        return ironoxide::get_flag(&aFlag3Txt, 11LL);
    }
  }
  return result;
}
```

Level one's decompiled code shows that it is trying to compare the user input with `v10`.

```c
__int64 ironoxide::level_one()
{
  __int64 v0; // x0
  _QWORD *v1; // x0
  __int64 v2; // x1
  __int64 v3; // x1
  __int64 v4; // x1
  unsigned int v6; // [xsp+Ch] [xbp-D4h]
  __int64 v7; // [xsp+20h] [xbp-C0h]
  __int64 v8; // [xsp+30h] [xbp-B0h]
  _BYTE v9[48]; // [xsp+50h] [xbp-90h] BYREF
  _QWORD v10[2]; // [xsp+80h] [xbp-60h] BYREF
  _QWORD v11[3]; // [xsp+90h] [xbp-50h] BYREF
  __int64 v12; // [xsp+A8h] [xbp-38h] BYREF
  _QWORD v13[2]; // [xsp+B0h] [xbp-30h] BYREF

  core::fmt::Arguments::new_const(&off_7C800);
  v0 = std::io::stdio::_print(v9);
  v10[0] = &aRustIsAnIronOx;
  v10[1] = 146LL;
  v1 = alloc::string::String::new(v11, v0);
  v12 = std::io::stdio::stdin(v1);
  v8 = std::io::stdio::Stdin::read_line(&v12, v11);
  core::result::Result<T,E>::expect(v8, v2, &aFailedToReadLi, 19LL, &off_7C810);
  v7 = <alloc::string::String as core::ops::deref::Deref>::deref(v11);
  v13[0] = core::str::<impl str>::trim(v7, v3);
  v13[1] = v4;
  v6 = core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq(v13, v10);
  core::ptr::drop_in_place<alloc::string::String>(v11);
  return v6;
}
```

Looking at the binary, `v10` is a string stored in the read-only data section of the binary.

```asm
.rodata:0000000000054FA9 aRustIsAnIronOx DCB "Rust is an iron oxide, a usually reddish-brown oxide formed by t"
.rodata:0000000000054FA9                                         ; DATA XREF: ironoxide::level_one+24↑o
.rodata:0000000000054FE9                 DCB "he reaction of iron and oxygen in the catalytic presence of wate"
.rodata:0000000000055029                 DCB "r or air moisture."
.rodata:000000000005503B aFailedToReadLi DCB "Failed to read line"
```

Send the string `Rust is an iron oxide, a usually reddish-brown oxide formed by the reaction of iron and oxygen in the catalytic presence of water or air moisture.` to get the first flag.

Level two's decompiled code shows that it calls a function `ironoxide::magic()` with a `v13`.

```c
bool ironoxide::level_two()
{
  __int64 v0; // x0
  __int64 v1; // x0
  _QWORD *v2; // x0
  __int64 v3; // x1
  __int64 v4; // x1
  __int64 v5; // x1
  _BOOL4 v7; // [xsp+4h] [xbp-16Ch]
  int v8; // [xsp+Ch] [xbp-164h]
  __int64 v9; // [xsp+18h] [xbp-158h]
  __int64 v10; // [xsp+28h] [xbp-148h]
  __int64 line; // [xsp+38h] [xbp-138h]
  _BYTE v12[52]; // [xsp+70h] [xbp-100h] BYREF
  unsigned int v13; // [xsp+A4h] [xbp-CCh] BYREF
  __int64 v14; // [xsp+A8h] [xbp-C8h] BYREF
  _BYTE v15[48]; // [xsp+B0h] [xbp-C0h] BYREF
  _OWORD v16[2]; // [xsp+E0h] [xbp-90h] BYREF
  _QWORD v17[3]; // [xsp+108h] [xbp-68h] BYREF
  _QWORD v18[2]; // [xsp+120h] [xbp-50h] BYREF
  __int64 v19; // [xsp+140h] [xbp-30h]
  __int64 v20; // [xsp+148h] [xbp-28h]
  __int128 v21; // [xsp+150h] [xbp-20h]

  core::fmt::Arguments::new_const(&off_7C870);
  v0 = std::io::stdio::_print(v12);
  v14 = rand::rngs::thread::thread_rng(v0);
  v13 = rand::rng::Rng::gen_range(&v14, 30LL, 40LL);
  core::ptr::drop_in_place<rand::rngs::thread::ThreadRng>(&v14);
  *&v21 = &v13;
  *(&v21 + 1) = core::fmt::num::imp::<impl core::fmt::Display for u32>::fmt;
  v16[1] = v21;
  v16[0] = v21;
  core::fmt::Arguments::new_v1(&off_7C880, v16);
  v1 = std::io::stdio::_print(v15);
  v2 = alloc::string::String::new(v17, v1);
  v18[0] = std::io::stdio::stdin(v2);
  line = std::io::stdio::Stdin::read_line(v18, v17);
  core::result::Result<T,E>::expect(line, v3, &aFailedToReadLi, 19LL, &off_7C8A0);
  v10 = <alloc::string::String as core::ops::deref::Deref>::deref(v17);
  v9 = core::str::<impl str>::trim(v10, v4);
  v19 = core::str::<impl str>::parse(v9, v5);
  v18[1] = v19;
  v20 = v19;
  v8 = core::result::Result<T,E>::expect(v19, &aNotANumber, 12LL, &off_7C8B8);
  v7 = v8 == ironoxide::magic(v13);
  core::ptr::drop_in_place<alloc::string::String>(v17);
  return v7;
}
```

`v13` is a random number between 30 and 40.
Decompiling the magic function and using a chat model like GPT-4o, it shows that it is a classic recursive fibonacci sequence.

```c
__int64 __fastcall ironoxide::magic(unsigned int a1)
{
  int v1; // w0
  int v2; // w0
  int v5; // [xsp+Ch] [xbp-24h]

  if ( a1 <= 1 )
  {
    return a1;
  }
  else
  {
    v1 = ironoxide::magic(a1 - 1);
    v5 = v1;
    if ( a1 < 2 )
      core::panicking::panic_const::panic_const_sub_overflow(&off_7C840);
    v2 = ironoxide::magic(a1 - 2);
    if ( __CFADD__(v5, v2) )
      core::panicking::panic_const::panic_const_add_overflow(&off_7C858);
    return (v5 + v2);
  }
}
```

Calculate the nth number (where n is the random number) of the fibonacci sequence to get the flag.

Level three requires both static and some dynamic reverse engineering.
The decompiled code shows a bunch of functions being run against a string

```c
__int64 ironoxide::level_three()
{
  __int64 v0; // x0
  _QWORD *v1; // x0
  __int64 v2; // x1
  __int64 v3; // x1
  __int64 v4; // x1
  __int64 v5; // x1
  __int64 v6; // x1
  __int64 v7; // x1
  unsigned int v9; // [xsp+4h] [xbp-1FCh]
  __int64 v10; // [xsp+18h] [xbp-1E8h]
  __int64 v11; // [xsp+28h] [xbp-1D8h]
  __int64 v12; // [xsp+38h] [xbp-1C8h]
  __int64 v13; // [xsp+48h] [xbp-1B8h]
  __int64 v14; // [xsp+58h] [xbp-1A8h]
  _BYTE v15[48]; // [xsp+78h] [xbp-188h] BYREF
  _QWORD v16[4]; // [xsp+A8h] [xbp-158h] BYREF
  _QWORD v17[3]; // [xsp+C8h] [xbp-138h] BYREF
  __int64 v18; // [xsp+E0h] [xbp-120h] BYREF
  __int64 v19[3]; // [xsp+E8h] [xbp-118h] BYREF
  __int64 v20[9]; // [xsp+100h] [xbp-100h] BYREF
  _QWORD src[9]; // [xsp+148h] [xbp-B8h] BYREF
  _QWORD v22[3]; // [xsp+190h] [xbp-70h] BYREF
  _QWORD v23[5]; // [xsp+1A8h] [xbp-58h] BYREF
  _QWORD v24[2]; // [xsp+1D0h] [xbp-30h] BYREF

  core::fmt::Arguments::new_const(&off_7C8D0);
  std::io::stdio::_print(v15);
  core::str::<impl str>::bytes(aTasty, 5LL);
  v0 = core::iter::traits::iterator::Iterator::cycle();
  v1 = alloc::string::String::new(v17, v0);
  v18 = std::io::stdio::stdin(v1);
  v14 = std::io::stdio::Stdin::read_line(&v18, v17);
  core::result::Result<T,E>::expect(v14, v2, aFailedToReadLi, 19LL, &off_7C8E0);
  v13 = <alloc::string::String as core::ops::deref::Deref>::deref(v17);
  v12 = core::str::<impl str>::trim(v13, v3);
  v11 = core::str::<impl str>::bytes(v12, v4);
  core::iter::traits::iterator::Iterator::zip(src, v11, v5, v16);
  core::iter::traits::iterator::Iterator::map(v20, src);
  core::iter::traits::iterator::Iterator::collect(v19, v20);
  alloc::string::String::from_utf8(v23, v19);
  core::result::Result<T,E>::expect(v22, v23, aInvalidUtf8, 13LL, &off_7C8F8);
  v10 = <alloc::string::String as core::ops::deref::Deref>::deref(v22);
  v24[0] = core::str::<impl str>::trim(v10, v6);
  v24[1] = v7;
  v9 = core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq(v24, &off_7C910);
  core::ptr::drop_in_place<alloc::string::String>(v22);
  core::ptr::drop_in_place<alloc::string::String>(v17);
  return v9;
}
```

There are 2 important variables here, `aTasty` and `off_7c910`.

```asm
.rodata:00000000000550B8 aTasty          DCB "tasty"             ; DATA XREF: ironoxide::level_three+24↑o

.rodata:00000000000550CA aRustWasCreated DCB "Rust was created because the creator had to climb 21 floors."
.rodata:00000000000550CA                                         ; DATA XREF: .data.rel.ro:off_7C910↓o
```

The cycle function clones the value of `tasty` as many times as required.
The map function is the most interesting, as it applies a function to a vector.

After stepping through the program, it enters the function `ironoxide::level_three::{{closure}}`.

The decompiled code shows that it's XOR-ing a single character with another character.

```c
__int64 __fastcall ironoxide::level_three::{{closure}}(__int64 a1, int a2, unsigned int a3)
{
  return a2 ^ a3;
}
```

Let's input a bunch of `A` characters and set a breakpoint in the comparison.

```asm
 ► 0xaaaaaaaa8bb4 <ironoxide::level_three+464>                                         bl     #core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq>
        x0: 0xffffffffd230 —▸ 0xaaaaaab23c50 ◂— '5 2585 2585 258'
        x1: 0xaaaaaab1c910 —▸ 0xaaaaaaaf50ca ◂— 0x7361772074737552 ('Rust was')
        x2: 0xf
        x3: 0xf
    ↓
   0xaaaaaaaab0f0 <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq>       str    x30, [sp, #-0x10]!
   0xaaaaaaaab0f4 <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+4>     mov    x9, x0
   0xaaaaaaaab0f8 <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+8>     mov    x8, x1
   0xaaaaaaaab0fc <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+12>    ldr    x0, [x9]
   0xaaaaaaaab100 <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+16>    ldr    x1, [x9, #8]
   0xaaaaaaaab104 <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+20>    ldr    x2, [x8]
   0xaaaaaaaab108 <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+24>    ldr    x3, [x8, #8]
   0xaaaaaaaab10c <core::cmp::impls::<impl core::cmp::PartialEq<&B> for &A>::eq+28>    bl     #core::str::traits::<impl core::cmp::PartialEq for str>::eq <core::str::traits::<impl core::cmp::PartialEq for str>::eq>
    ↓
   0xaaaaaaaaca70 <core::str::traits::<impl core::cmp::PartialEq for str>::eq>         sub    sp, sp, #0x30
   0xaaaaaaaaca74 <core::str::traits::<impl core::cmp::PartialEq for str>::eq+4>       str    x30, [sp, #0x20]
```

There seems to be a repeating pattern every 5 characters.
It is probably trying to XOR our user input with the word `tasty`.

Let's try in Python to verify.

```python
from pwn import *
xor(b'tasty', b'AAAAAAAAAA')
```

```text
b'5 2585 258'
```

We can see that it has the same output.
Now all we have to do is to XOR `Rust was created because the creator had to climb 21 floors.` with tasty and send that as the input to get the flag.

```python
from pwn import *
xor(b'tasty', b'Rust was created because the creator had to climb 21 floors.')
```

```text
>>> xor(b'tasty', b'Rust was created because the creator had to climb 21 floors.')
b'&\x14\x00\x00Y\x03\x00\x00T\x1a\x06\x04\x12\x00\x1c\x10A\x11\x11\x1a\x15\x14\x00\x11Y\x00\t\x16T\x1a\x06\x04\x12\x00\x16\x06A\x1b\x15\x1dT\x15\x1cT\x1a\x18\x08\x1e\x16YFPS\x12\x15\x1b\x0e\x01\x07W'
```

### Flag

- `CyberBlitz{rust_makes_malware_reverse_engineering_10x_harder}`
- `CyberBlitz{imagine_trademarking_the_name_rust}`
- `CyberBlitz{youtu.be/watch?v=03H1cWj2Kfc}`
