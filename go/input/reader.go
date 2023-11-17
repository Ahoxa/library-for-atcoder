package main

import (
    "bufio"
    "os"
    "fmt"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n') // 改行文字まで読み込む
    fmt.Print(text)                    // 読み込んだ内容を出力
}
