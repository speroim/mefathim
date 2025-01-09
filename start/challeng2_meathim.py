def count_inversions(arr):              # מתחיל פונקציה לספירת היפוכים
    inversions = 0                      # קביעת ברירת מחדל 0 היפוכים
    n = len(arr)                        # הצבת אורך המערך כמשתנה בשם N
    for i in range(n):                  # לכל מספר / אובייקט במערך מתוך אורך המערך שיקרא בשם I
        for j in range(i+1, n):         # לעבור כל שאר המספרים שנמצאים בהמשך המערך אחרי I
            if arr[i] > arr[j]:         # אם האובייקטים מצד ימין למשתנה גדולים מהאובייקט הנוכחי
                inversions += 1         # תוסיף עוד היפוך לתוצאה
    return inversions                   # הפונקציה תחזיר את סה"כ ההיפוכים

# Example usage
arr = [2, 4, 1, 5, 3]
print(f"Number of inversions: {count_inversions(arr)}")