use std::io;

fn main() {

    get_secret_codes();

}

fn get_secret_codes() {
   let player = ["Red", "Yellow", "Blue", "Green"];
   let mut index = 0;

   while index < 4 {
      println!("{} player, enter secret code.", player[index]);

            let mut player_code = String::new();
         
            io::stdin()
               .read_line(&mut player_code)
               .expect("Failed to read line");
               .trim();
               
       println!("The secret code for {} player, is {}:", player[index], player_code);
       
       index = index + 1
       
    } // End index loop
} // End get_secret_codes()


// TODO
// - Limit secret codes to: 
// 	 	code_permutations = vec![00, 01, 02, 10, 11, 12, 20, 21, 22]
// - Build a list of players based on whether or not they pass
// 	 	Only players that input a secret code, should be counted.

