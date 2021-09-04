use std::io;

fn main() {
    let mut input_text = String::new();
    io::stdin().read_line(&mut input_text).expect("error");
    let trimmed = input_text.trim();

    let mut n:i64 = 0;

    match trimmed.parse::<i64>() {
        Ok(i) => n = i,
        Err(_) => println!("this was not an integer: {}", trimmed),
    };

    let mut s = String::new();

    loop {        
        if n % 2 == 0 {
            s = "B".to_string() + &s;
            n = n / 2;
        }
        else {
            s = "A".to_string() + &s;
            n = n - 1;
        }

        if n == 0 {
            break;
        }
    }

    println!("{}", s)
}