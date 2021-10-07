package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
)

func main() {

	var json_str string

	var n int

	fmt.Scan(&n)
	sc := bufio.NewScanner(os.Stdin)

	for i := 0; i <= n; i++ {

		sc.Scan()
		json_str += sc.Text()
	}

	var obj []interface{}
	var my_set = make(map[string]bool)

	json.Unmarshal([]byte(json_str), &obj)

	for i := 0; i < len(obj); i++ {
		data := obj[i].(map[string]interface{})
		key := data["data"].(map[string]interface{})
		value := key["key"]
		my_set[value.(string)] = true

	}

	fmt.Println(len(my_set))

}
