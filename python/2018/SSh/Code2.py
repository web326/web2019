def sftp_walkdir(sftp, path):
    '''
    递归获取path下的所有文件与目录
    :param sftp: python ssh sftp object
    :param path:
    :return:
    '''
    now_dirname = os.path.split(path)[-1]
    backups = []
    files = sftp.listdir_attr(path)
    for f in files:
        tpath = "{}/{}".format(path, f.filename)
        if f.longname[0] == "d":

            r = sftp_walkdir(sftp, tpath)
            backups.append(r)
        else:
            backups.append({"filename":f.filename, "_path_":tpath})

    return {now_dirname:backups, "_path_":path}

# 测试下
# 连接远程服务器
client = connect_host(192.168.1.111,  22,  "test",  "123456")
r = sftp_walkdir(sftp, "/home/work/sshtest")
print(json.dumps(r, sort_keys=True, indent=2))

{
  "_path_": "/home/work/sshtest",
  "sshtest": [
    {
      "_path_": "/home/work/sshtest/test2.txt",
      "filename": "test2.txt"
    },
    {
      "_path_": "/home/work/sshtest/test1.txt",
      "filename": "test1.txt"
    },
    {
      "_path_": "/home/work/sshtest/sshtest_222",
      "sshtest_222": [
        {
          "_path_": "/home/work/sshtest/sshtest_222/test_lalalal.txt",
          "filename": "test_lalalal.txt"
        },
        {
          "_path_": "/home/work/sshtest/sshtest_222/sshtest_333_222",
          "sshtest_333_222": [
            {
              "_path_": "/home/work/sshtest/sshtest_222/sshtest_333_222/test_ooooo.txt",
              "filename": "test_ooooo.txt"
            }
          ]
        },
        {
          "_path_": "/home/work/sshtest/sshtest_222/sshtest_333",
          "sshtest_333": []
        },
        {
          "_path_": "/home/work/sshtest/sshtest_222/test_hahahah.txt",
          "filename": "test_hahahah.txt"
        }
      ]
    }
  ]
}
