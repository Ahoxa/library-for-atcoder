package main

import "fmt"

func main() {
    var a int
    var b string
    fmt.Scan(&a)       // 整数を読み込む
    fmt.Scanln(&b)     // 文字列を読み込む
    fmt.Println(a, b)  // 読み込んだ内容を出力
}
