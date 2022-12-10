# coding=utf-8

import pandas as pd

if __name__ == '__main__':
    # 文件名
    filename = 'example.csv'
    write_filename = 'index.html'
    # 读取文件
    dataframe = pd.read_csv(filename)
    webfile = open(write_filename, "r", encoding="utf-8")
    content = webfile.read()
    webfile.close()

    # 获取目录插入位置
    pos = content.find("<ul id=\"main-menu\" class=\"main-menu\">")

    # 目前目录项
    catalogues = set()
    for catalogue in dataframe['type']:
        catalogues.add(catalogue)
    catalogues = list(catalogues)
    catalogues.sort()
    print(catalogues)

    # 插入目录项
    strings = """"""
    for catalogue in catalogues:
        strings += '''
                    <li>
                        <a href="#{}" class="smooth">
                            <span class="title" style="font-size:20px">{}</span>
                        </a>
                    </li>'''.format(catalogue, catalogue)
    content = content[:pos+37] + strings + content[pos+37:]


    # 插入具体内容位置
    pos = content.find("<div class=\"main-content\">")

    # 插入具体项
    strings = """"""
    flag = 0
    for catalogue in catalogues:
        strings += """
            <h4 class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id="{}"></i>{}</h4>
            """.format(catalogue, catalogue)
        for row, value in dataframe.iterrows():
            if value['type'] == catalogue:
                if flag == 0:
                    strings += """<div class="row">"""
                strings += """
                <div class="col-sm-3">
                    <div class="xe-widget xe-conversations box2 label-info" onclick="window.open('{}', '_blank')" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="{}">
                        <strong>{}</strong>
                        <p class="overflowClip_2">{}</p>
                    </div>
                </div>""".format(value['site'], value['tool'], value['site'], value['description'])
                flag += 1
                if flag == 4:
                    strings += """</div>"""
                    flag = 0
        if flag != 0:
            strings += """</div>"""
            flag = 0

    content = content[:pos+26] + strings + content[pos+26:]

    webfile = open(write_filename, "w", encoding="utf-8")
    webfile.write(content)
    webfile.close()
