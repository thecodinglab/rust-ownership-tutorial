# Ownership & Borrowing in Rust

Tutorial for *Programming Languages and Paradigms* (UZH), 11.11.2026,
by Florian Walter and Anto Grgic.

We port a small Python bank program to Rust and let the borrow checker
show us what Rust's ownership model enforces.

## Before the tutorial

1. Read the preparation document: [`prep/preparation.pdf`](prep/preparation.pdf)
   (installing Rust, editor setup, warm-up reading).
2. Try the starter code:

   ```sh
   cd code/rust
   cargo run      # fails with E0382: intended, this is where we start
   ```

`code/python/bank.py` is the Python program we port, and
[`slides/slides.pdf`](slides/slides.pdf) are the slides.
