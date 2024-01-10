import requests
import tkinter as tk
#初始化tkinter
win = tk.Tk()
win.title('text')
win.geometry('800x800')
def question():
    #update
    global Question_Entry
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    up_url = 'https://www.baidu.com/s?tn=22073068_8_oem_dg&ch=2&ie=utf-8&word='
    need_index_word_to_url = Question_Entry.get()
    up_url += need_index_word_to_url
    r = requests.get(up_url,headers=headers)
    url_backcode = r.text
    writer = open('baidu.html.txt','w',encoding='utf-8')
    writer.write(url_backcode)
    writer.close()

    url_code = open('baidu.html.txt','r',encoding='utf-8')
    url_codes = (url_code.read()).split('\n')
    ans = []
    for i in url_codes:
        if '<span class="content-right_8Zs40">' in i:
            ans.append(i)
    compelete_things = []
    for i in ans:
        first_i = i.split('<span class="content-right_8Zs40">')[1] #['222','111']
        second_i = first_i.split('</span>')[0]
        compelete_things.append(second_i)
    finals = []
    for i in compelete_things:
        first_i = i.split('。')
        next = first_i[:-1]
        final = '。'.join(next) + '。'
        finals.append(final)
    finally_complete_ans = []
    for i in finals:
        f = i.split('<em>')
        f = ''.join(f)
        f2 = f.split('</em>')
        f2 = ''.join(f2)
        finally_complete_ans.append(f2)
    real_best_ans = finally_complete_ans[0]
    if real_best_ans == '。':
        real_best_ans = '6'
    print(real_best_ans)
#数据处理&爬虫部分完成
    ANS_Label.config(text='回答:'+real_best_ans)
    url_code.close()

#tkinter
First_Label = tk.Label(win,text='Text')
First_Label.pack()
Question_Entry = tk.Entry(win,width=40)
Question_Entry.pack()
Search_question_Button = tk.Button(win,text='提问',command=question)
Search_question_Button.pack()
ANS_Label = tk.Label(win,text='回答:')
ANS_Label.pack()
win.mainloop()