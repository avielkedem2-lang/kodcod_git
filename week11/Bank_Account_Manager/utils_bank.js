import {deposit, Withdraw} from "./bank_manager.js"
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


function isCustomerActive(customer){
    if (customer.isActive){
        return true
    }
}




export function sandToDposit(){
    const id = rl.questionInt("Enter id: ")
    const customer = isCustomer(id.toString())
    if (customer){
        if (isCustomerActive(customer)){
            const amount = rl.questionInt("Enter amount: ")
            if (depositValidation(amount)){
                deposit(id, amount, customer)
                return "Deposit completed successfully"
            }else{
                console.log("The amount most to be bigger than 0")
            }
        }else{
            console.log("The customer not active!")
        }
    }
} 









function WithdrawValdition(amount, customer){
    if (amount > 0){
        if (amount <= customer.balance)
            return true
    }
}






export function sandToWithdraw(){
    const id = rl.questionInt("Enter id: ")
    const customer = isCustomer(id.toString())
    if (customer){
        if (isCustomerActive(customer)){
            const amount = rl.questionInt("Enter amount: ")
            if (WithdrawValdition(amount, customer)){
                Withdraw(id, amount, customer)
            }else{
                console.log("The amount is not bigger than 0 or amount bigger than balance")
            }

        }else{
            console.log("The customer not active!")
        }
    }
} 






