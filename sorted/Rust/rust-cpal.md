# Rust - cpal

## conv

in cpal there is a macro defined as following:

```rust
macro_rules! impl_from_sample {
    ($T:ty, $fn_name:ident from $({$U:ident: $Umod:ident})*) => {
        $(
            impl FromSample<$U> for $T {
                #[inline]
                fn from_sample_(s: $U) -> Self {
                    self::$Umod::$fn_name(s)
                }
            }
        )*
    };
}
```

Job that macro does is:

```rust
impl_from_sample! {i64, to_i64 from
{i8:i8} {i16:i16} {I24:i24} {i32:i32} {I48:i48}
{u8:u8} {u16:u16} {U24:u24} {u32:u32} {U48:u48} {u64:u64}
{f32:f32} {f64:f64}
}
```

- Above code will expand to following code
- Which implements the trait `FromSample<T>` for primitive type `i64` for all sample types `T` defined in the macro invocation

```rust
impl FromSample<i8> for i64 {
    #[inline]
    fn from_sample_(s: i8) -> Self {
        self::i8::to_i64(s)
    }
}

impl FromSample<i16> for i64 {
    #[inline]
    fn from_sample_(s: i16) -> Self {
        self::i16::to_i64(s)
    }
}

impl FromSample<I24> for i64 {
    #[inline]
    fn from_sample_(s: I24) -> Self {
        self::i24::to_i64(s)
    }
}

impl FromSample<i32> for i64 {
    #[inline]
    fn from_sample_(s: i32) -> Self {
        self::i32::to_i64(s)
    }
}

impl FromSample<I48> for i64 {
    #[inline]
    fn from_sample_(s: I48) -> Self {
        self::i48::to_i64(s)
    }
}

impl FromSample<u8> for i64 {
    #[inline]
    fn from_sample_(s: u8) -> Self {
        self::u8::to_i64(s)
    }
}

impl FromSample<u16> for i64 {
    #[inline]
    fn from_sample_(s: u16) -> Self {
        self::u16::to_i64(s)
    }
}

impl FromSample<U24> for i64 {
    #[inline]
    fn from_sample_(s: U24) -> Self {
        self::u24::to_i64(s)
    }
}

impl FromSample<u32> for i64 {
    #[inline]
    fn from_sample_(s: u32) -> Self {
        self::u32::to_i64(s)
    }
}

impl FromSample<U48> for i64 {
    #[inline]
    fn from_sample_(s: U48) -> Self {
        self::u48::to_i64(s)
    }
}

impl FromSample<u64> for i64 {
    #[inline]
    fn from_sample_(s: u64) -> Self {
        self::u64::to_i64(s)
    }
}

impl FromSample<f32> for i64 {
    #[inline]
    fn from_sample_(s: f32) -> Self {
        self::f32::to_i64(s)
    }
}

impl FromSample<f64> for i64 {
    #[inline]
    fn from_sample_(s: f64) -> Self {
        self::f64::to_i64(s)
    }
}
```
