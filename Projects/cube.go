package main

import "fmt"

func main() {

    var num int

    fmt.Print("Enter the Number to find Cube = ")
    fmt.Scanln(&num)

    cube := num * num * num

    fmt.Println("\nThe Cube of a Given Number  = ", cube)
}
