import {deposit} from "./bank_manager.js"
import { searchCustomer } from "./customer_manager.js"
import rl from "readline-sync"


function depositValidation(amount){
    if (amount > 0){
        return true
    }
}


function isCustomer(id){
    const customer = searchCustomer(id)
    if (customer){
        return customer
    }else {
        console.log(`The id= ${id} not fond!`)
    }
}



export function sandToDposit(){
    const id = rl.questionInt("Enter id: ")
    const customer = isCustomer(id.toString())
    if (customer){
        const amount = rl.questionInt("Enter amount: ")
        if (depositValidation(amount)){
            deposit(id, amount, customer)
            return "Deposit completed successfully"
        }else{
            console.log("The amount most to be bigger than 0")
        }
    }
} 