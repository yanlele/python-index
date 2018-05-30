查看你的python所支持的whl 文件类型（非常重要，否则会发生：* is not a supported wheel on this platform错误）

在shell中输入
```python
import pip
print(pip.pep425tags.get_supported())
```