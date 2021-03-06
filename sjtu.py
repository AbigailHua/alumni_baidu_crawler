# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import os
import re


def delete_redundent(s):
    s = re.sub(r'\n+', "\n", s)
    return s.strip()


def openFile(path):
    if path.endswith('txt'):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.readlines()
        return content
    return


def get_page(page):
    try:
        for i in range(3):
            r = requests.get(url=page, headers=headers)
            r.encoding = r.apparent_encoding
            print("Requesting ", r.url)
            if r.status_code == 200:
                if r.url.find("wappass.baidu.com") != -1:
                    print("Blocked by Baidu!")
                    for t in range(6):
                        time.sleep(100)
                        print("Sleep countdown: {} mins...".formate(6-t))
                else:
                    return r.text
            else:
                continue
        print("Failed to get url "+page)
        return ""
    except Exception as e:
        print(e)
        time.sleep(2)
        return ""


def formatFileName(s):
    invalid_chars = "<>/\|:*?\n"
    s = ''.join(c for c in s if c not in invalid_chars)
    s = s.strip()
    if len(s) > 255:
        s = s[:255]
    return s


def savePage(name, title, url):
    idx_filename = 'index.txt'
    folder = 'html'
    subfolder = os.path.join(folder, name)
    filename = formatFileName(title)
    filename += ".txt"
    if not os.path.exists(folder):
        os.mkdir(folder)
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    content = get_page(url)
    time.sleep(2)
    if content:
        soup = BeautifulSoup(content, "html.parser")
        fr = soup.get_text()
        fr = delete_redundent(fr)
        f = open(os.path.join(subfolder, filename), 'w', encoding="utf-8")
        f.write(fr)
        f.close()
        index = open(idx_filename, 'a', encoding="utf-8")
        index.write(title + '\t' + filename + '\t' + url + '\n')
        index.close()


def spider(name):
    return_dict = {}
    word = "%2B\""+name+"\"%2B上海交通大学"
    url = u'http://www.baidu.com.cn/s?wd=' + word + '&cl=3'
    try:
        content = get_page(url)
        if content:
            soup = BeautifulSoup(content, 'html.parser', from_encoding="utf-8")
            for item in soup.find_all('h3', class_='t'):
                a = item.a
                link = a['href']
                title = a.text
                if title and link:
                    return_dict[title] = link
                    print(link)
                    print(title)
                    print("----------------------------------------------------")
                    savePage(name, title, link)
    except Exception as e:
        print("Error: ", e)
        time.sleep(2)
    return return_dict


def run(file_path):
    result = {}
    foo = openFile(file_path)
    if foo:
        for line in foo:
            line = line.strip()
            if line:
                result[line] = spider(line)
                time.sleep(5)


if __name__ == '__main__':
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    run("name.txt")
