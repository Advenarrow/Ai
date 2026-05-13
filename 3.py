import pandas as pd
import math
import matplotlib.pyplot as plt

# Sample Data
data = { 
    'word': ['free', 'win', 'prize', 'lottery', 'meet', 'class', 'hello'], 
    'spam_count': [5, 4, 3, 2, 0, 0, 0], 
    'ham_count': [0, 0, 0, 1, 4, 3, 5] 
} 
df = pd.DataFrame(data) 

# Totals for calculation 
total_spam = df['spam_count'].sum() 
total_ham = df['ham_count'].sum() 
vocab_size = len(df) 

def classify_word(word): 
    word = word.lower() 
    log_spam = math.log(0.5) 
    log_ham = math.log(0.5) 
    
    if word in df['word'].values: 
        row = df[df['word'] == word].iloc[0] 
        p_spam = (row['spam_count'] + 1) / (total_spam + vocab_size) 
        p_ham = (row['ham_count'] + 1) / (total_ham + vocab_size) 
    else: 
        p_spam = 1 / (total_spam + vocab_size) 
        p_ham = 1 / (total_ham + vocab_size) 
        
    log_spam += math.log(p_spam) 
    log_ham += math.log(p_ham) 
    
    prob_spam = math.exp(log_spam)
    prob_ham = math.exp(log_ham)
    total_prob = prob_spam + prob_ham
    return ("spam" if log_spam > log_ham else "not spam"), prob_spam/total_prob, prob_ham/total_prob

# Run test
test_word = 'free' # You can change this to test other words
result, ps, ph = classify_word(test_word)
print(f"Word: {test_word} -> Result: {result}")

plt.bar(['Spam', 'Not Spam'], [ps, ph], color=['red', 'blue'])
plt.title(f'Naive Bayes: "{test_word}"')
plt.ylabel('Probability')
plt.show()