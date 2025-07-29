# Force Push Test Repository 🔍

Ye ek test repository hai jo **Force Push Scanner** tool ko test karne ke liye banaya gaya hai.

## Purpose 
Is repo mein deliberately secrets add kiye gaye hain testing ke liye, taki hum verify kar saken ki hamara force-push-scanner tool properly kaam kar raha hai.

## Test Files
- `config.py`: Database credentials aur API keys
- `.env`: Environment variables with sensitive data

## ⚠️ Warning
Ye test data hai - real production secrets nahi hain!

## Testing Process
1. Secrets add karo
2. Commit karo  
3. Force push scenario create karo
4. Scanner tool run karo
5. Results verify karo