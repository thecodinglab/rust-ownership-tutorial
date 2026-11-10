struct Account {
    owner: String,
    balance: i64,
}

impl Account {
    fn new(owner: &str, balance: i64) -> Account {
        Account { owner: owner.to_string(), balance }
    }
}

fn print_report(accounts: Vec<Account>) {
    for a in accounts {
        println!("  {:<10} {:>6}", a.owner, a.balance);
    }
}

fn main() {
    let accounts = vec![
        Account::new("alice", 100),
        Account::new("bob", 50),
        Account::new("carol", 0),
        Account::new("dave", 0),
    ];

    println!("Opening balances:");
    print_report(accounts);

    // TODO: transfer, richest, close_empty

    println!("After closing empty accounts:");
    print_report(accounts);
}
