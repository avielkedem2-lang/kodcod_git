import rl from "readline-sync"
import {createId, saveCustomer} from "./customer_manager.js";
import {sendToCreateCustomer} from "./utils.js"


const inc = createId()
const save = saveCustomer()

while (true){
    let userChoice = rl.questionInt("Enter your choice: ")
    if (userChoice === 1){
        
        let customer = sendToCreateCustomer(inc())
        if (customer){
            save.addCustomer(customer)
        }
        

    }else if (userChoice === 2){
       save.getAllCustomers() 
    }else if (userChoice === 0){
        break
    }


}
