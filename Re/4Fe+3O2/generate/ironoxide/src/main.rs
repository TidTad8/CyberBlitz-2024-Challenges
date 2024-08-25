use rand::Rng;
use std::fs;
use std::io;

fn level_one() -> bool {
    println!("======== Level One ========");

    let rust = "Rust is an iron oxide, a usually reddish-brown oxide formed by the reaction of iron and oxygen in the catalytic presence of water or air moisture.";

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    input.trim() == rust
}

fn magic(num: u32) -> u32 {
    if num <= 1 {
        return num;
    }

    return magic(num - 1) + magic(num - 2);
}

fn level_two() -> bool {
    println!("======== Level Two ========");

    let random_number = rand::thread_rng().gen_range(30..40);
    println!("Here's your magic number: {}", random_number);

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    let input = input.trim().parse::<u32>().expect("Not a number");

    return input == magic(random_number);
}

fn level_three() -> bool {
    println!("======= Level Three =======");

    let key = "tasty".bytes().cycle();

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let unencrypted_bytes = input
        .trim()
        .bytes()
        .zip(key)
        .map(|(byte, key_byte)| byte ^ key_byte)
        .collect();

    let text = String::from_utf8(unencrypted_bytes).expect("Invalid UTF-8");

    return text.trim() == "Rust was created because the creator had to climb 21 floors.";
}

fn get_flag(flag_name: &str) {
    let contents = fs::read_to_string(flag_name)
        .expect("If you're seeing this instead of the flag, please contact an administrator");

    println!("Congratulations! Here is your flag: {}", contents.trim());
}

fn main() {
    if !level_one() {
        return;
    }
    get_flag("./flag1.txt");

    if !level_two() {
        return;
    }
    get_flag("./flag2.txt");

    if !level_three() {
        return;
    }
    get_flag("./flag3.txt");
}
