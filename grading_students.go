package main

import "fmt"

const noRoundingThreshold = 38

func main() {
	grades := []int32{73, 67, 38, 33}
	result := gradingStudents(grades)

	fmt.Println(result)
}

func round(n int32) int32 {
	a := (n / 5) * 5
	b := a + 5

	if (n - a) > (b - n) {
		return b
	}

	return a
}

func gradingStudents(grades []int32) []int32 {
	var final []int32

	for _, g := range grades {
		if g < noRoundingThreshold {
			final = append(final, g)
		} else {
			rounded := round(g)

			if (rounded-g) < 3 && (rounded-g) > 0 {
				final = append(final, rounded)
			} else {
				final = append(final, g)
			}
		}
	}

	return final
}
