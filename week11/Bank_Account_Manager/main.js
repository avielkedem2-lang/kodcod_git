import rl from "readline-sync"
import {createId, save} from "./customer_manager.js";
import {sendToCreateCustomer, sandToSearchCustomer, closeAccountValdition} from "./utils_customer.js"
import { sandToDposit , sandToWithdraw} from "./utils_bank.js";


const inc = createId()
// const save = saveCustomer()

let exit = true

while (exit){
    let userChoice = rl.questionInt("Enter your choice: ")


    if (userChoice === 1){
        let customer = sendToCreateCustomer(inc())
        if (customer){
            save.addCustomer(customer)
            console.log("Customer created successfully")
        }
        

    }else if (userChoice === 2){
       console.log(save.getAllCustomers()) 
    
    
    }else if (userChoice === 3){
        console.log(sandToSearchCustomer())
    
    }else if (userChoice === 4){
        sandToDposit()
    
    }else if (userChoice === 5){
        sandToWithdraw()
    
    }else if(userChoice === 6){
        closeAccountValdition()
        console.log("Account closed successfully")

    }else if (userChoice === 0){
        exit = false
    }


}
