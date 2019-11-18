---
{{ $pn := index (split .TranslationBaseName "-") 0 | replaceRE "^p" "" -}}
{{ $vol := print "v" (div (int $pn) 100) -}}
{{ $title := .TranslationBaseName -}}

title: "{{ replace $title "-" " " | replaceRE "^p" "UVa " | title }}"
author: "Kevin Cheng"
tags: ["UVa", "{{ $vol }}", "wip"]
date: {{ .Date }}
draft: true
---

# 題目


<!--more-->

# Input


# Output


# 解法


# Source Code

{{ $existed := false -}}
{{ range $key, $ext := (dict "py3" ".py" "c++" ".cpp" "c" ".c" "java" ".java" ) -}}
	{{- $path := (path.Join "uva" $vol (print $title $ext)) -}}
	{{- if and ((fileExists $path) (eq $existed false)) -}}
{{< readfile file="{{$path}}" highlight="{{$key}}" >}}
		{{- $existed = true -}}
	{{- end -}}
{{ end -}}
{{- if eq $existed false -}}
<!-- < readfile file="uva/OOXX" highlight="OOXX" > -->
{{- end -}}

