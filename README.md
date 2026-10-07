# legacy-outsource (private)

2019~2020년 외주·과제 코드 보관용 저장소. 각 폴더는 원래 별도 저장소였고, 커밋 히스토리를 유지한 채 합쳤습니다.

| 폴더 | 원래 저장소 |
|---|---|
| `outsource/` | `outsource` + `algorithm2` (`async`, `konlpy`는 `algorithm2` 히스토리에 이미 포함) |
| `web/` | `web` |
| `outsource-python3.6/` | `outsource_python3.6` |
| `unixlinux/` | `UnixLinux` |

합치면서 제외한 것: `venv/`, `node_modules/`, `.idea/`, `*.pem`, `*.exe|*.dll|*.pyd|*.pyc`, 50MB 초과 파일(`os_clinux/2/NY.tgz`),
dependabot 브랜치. 텔레그램 봇 토큰과 Django `SECRET_KEY`는 치환했습니다.
