

function saveCustomer() {
  let customers = []
  function addCustomer(customer) {
    customers.push(customer)
  }
  function getAllCustomers(){
    return customers
  }
return {addCustomer, getAllCustomers}
}


export const save = saveCustomer()

export function createId() {
  let id = 0
  function increment() {
    return ++id
  }
  return increment
}



export function createCustomer(id, name, accountType, balance) {
  const newCustomer = {
    id: id.toString(),
    fullName: name,
    accountType: accountType,
    balance: balance,
    isActive: true
  }
  return newCustomer
}







export function searchCustomer(val){
  const allCustomers = save.getAllCustomers()
  const isId = allCustomers.find((customer) => {
    return customer.id === val || customer.fullName.toLowerCase() === val.toLowerCase()
  })
  return isId
}


