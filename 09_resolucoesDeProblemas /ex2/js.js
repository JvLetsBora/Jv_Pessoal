function troca(){
    let m1 = document.getElementById("m1").value // e
    let m2 = document.getElementById("m2").value // b
    var save // NaH
    save = m1 // e
    m1 = m2 // b
    m2 = save // e
    document.getElementById("m1").value = m1
    document.getElementById("m2").value = m2
}