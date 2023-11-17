package main

import (
    "bufio"
    "os"
    "fmt"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)

    for scanner.Scan() {
        line := scanner.Text() // ここで1行ずつ読み込み
        fmt.Println(line)      // 読み込んだ行を出力（必要に応じて処理）
    }

    if err := scanner.Err(); err != nil {
        fmt.Fprintln(os.Stderr, "読み込みエラー:", err)
    }
}
