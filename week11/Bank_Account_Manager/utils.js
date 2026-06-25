import {createCustomer} from "./customer_manager.js"
import rl from "readline-sync"


function nameValidation(name){
    if (name){
        return true
    }
    return false
}


function accountTypeValdation(accountType){
    const onlyTypeAccount = ["Regular", "Premium", "Student"]
    return onlyTypeAccount.find((val) => {
        return accountType === val
    })
}


function balanceValdation(balance){
    if (balance >= 0){
        return true
    }
    return false
}



export function sendToCreateCustomer(id){
    const name = rl.question("Enter your name: ");
    if (nameValidation(name)){
        const accountType = rl.question("Enter your type account: ");

        if (accountTypeValdation(accountType)){
            const balance = rl.questionInt("Enter tour balance: ");

            if (balanceValdation(balance)){
                return createCustomer(id, name, accountType, balance)
            }
            else {
                console.log("balance most to be 0 or more")
            }

        }
        else{
            console.log(`account cna't be ${accountType}`)
        }
    }
    else{
        console.log( "name most to be a word")
    }
}


// let a = "a";
// const arr = ["3", "c"]
// const d = arr.find((val) => {
//     return a === val
// })
// console.log(d)