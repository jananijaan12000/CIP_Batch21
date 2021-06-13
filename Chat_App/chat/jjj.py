def output_lable(n):
  if n == 1:
    return "Offensive "
  elif n ==0:
    return "Not Offensive "

def manual_testing(news):
  testing_news = {"text":[news]}
  new_def_test = pd.DataFrame(testing_news)
  new_def_test["text"] = new_def_test["text"]
  new_x_test = new_def_test["text"]
  new_xv_test = tfidf_vect.transform(new_x_test)
  pred_sgdc = model.predict(new_xv_test)
  return pred_sgdc

words=news.split()
words2 =[]
for x in words:
  res=manual_testing(x)
  if res == 1:
     words2.append('****')
  else:
     words2.append(x)

s=' '.join(words2)
return s       