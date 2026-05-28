# 工时周报重构方案 — 沟通目录

> 本目录用于团队详细讨论 **工时周报系统智能化重构** 的新方案，沉淀背景、对标、设计、架构与实施计划。

**创建日期：** 2026-05-26  
**状态：** 🟡 方案讨论中

---

## 在线预览

| 页面 | 内网预览 | GitHub Pages（飞书文档可外链） |
|------|----------|-------------------------------|
| **导航入口** | http://preview.rigol.com/u/sn04077/timesheet-redesign/ | **https://piyansheng.github.io/timesheet-redesign/** |
| 流程汇报 | http://preview.rigol.com/u/sn04077/timesheet-redesign/汇报-工时数据流与业务流程.html | https://piyansheng.github.io/timesheet-redesign/汇报-工时数据流与业务流程.html |
| UX 原型 | http://preview.rigol.com/u/sn04077/timesheet-redesign/prototypes/ | https://piyansheng.github.io/timesheet-redesign/prototypes/ |
| **整合提交页** | — | **https://piyansheng.github.io/timesheet-redesign/prototypes/unified-weekly-submit.html** |

- 内网部署：`python scripts/deploy_to_preview.py`
- GitHub 部署：复制静态文件到 `piyansheng.github.io/timesheet-redesign/` 后 push

---

## 汇报用流程图

| 文件 | 说明 |
|------|------|
| [`汇报-工时数据流与业务流程.html`](汇报-工时数据流与业务流程.html) | **预填来源 + 员工/PM 全流程框图（浏览器打开即可演示）** |

---

## UX 范式可视化原型

五种填报页面 HTML mockup（浏览器直接打开）：

| 范式 | 文件 | 说明 |
|------|------|------|
| 导航 | [`prototypes/index.html`](prototypes/index.html) | **从这里开始（可交互 v2）** |
| 提交后 | `prototypes/flow-submitted.html` | 员工提交成功 + Booking 拆分 |
| 个人记录 | `prototypes/flow-personal-records.html` | 提交后查询状态 |
| PM 队列 | `prototypes/flow-pm-queue.html` | 超 Booking 待审批 |
| A | `prototypes/paradigm-a-draft-review.html` | 草稿确认页（主推荐） |
| B | `prototypes/paradigm-b-assist-grid.html` | Assist 弹窗 + Grid |
| C | `prototypes/paradigm-c-timeline.html` | 日历时间轴（移动） |
| D | `prototypes/paradigm-d-card-mywork.html` | 卡片 My Work |
| E | `prototypes/paradigm-e-bot-chat.html` | Bot 对话记工 |

---

## 关联资料

| 资料 | 链接/路径 |
|------|-----------|
| 现有需求文档（PRD 基线） | [飞书：工时系统功能需求文档](https://rigolportal.feishu.cn/wiki/V3ClwcvW5iEvbDkksyOcH4DKnvd) |
| PRD 差距分析表 | [飞书：差距分析](https://www.feishu.cn/wiki/Tg05wcHMYiCX9wk4PGpctgFtnrc) |
| 行业研究（本地） | `C:\Users\sn04077\Documents\Timesheet_System_Research_20260526\` |
| 差距分析（本地备份） | `../docs/timesheet_prd_gap_analysis.md` |

---

## 目录结构

```
timesheet-redesign/
├── README.md                          ← 你在这里（总导航）
├── 00-背景与目标/
│   └── 01-项目背景与重构目标.md
├── 01-现状分析/
│   ├── 01-现状问题与用户反馈.md
│   └── 02-现有能力清单（保留项）.md
├── 02-行业对标/
│   └── 01-标杆填报UX与AI能力.md
├── 03-新方案设计/                     ← 核心讨论区
│   ├── 00-设计原则与产品愿景.md
│   ├── 01-填报体验新方案（草稿优先）.md
│   ├── 02-代发与日程确认方案.md
│   ├── 03-接收审批与Booking规则.md
│   ├── 04-移动端方案.md
│   ├── 05-报表与分析方案.md
│   └── 06-AI能力路线图.md
├── 04-技术架构/
│   ├── 01-目标架构与飞书集成.md
│   └── 02-数据模型草案.md
├── 05-实施计划/
│   ├── 01-分阶段里程碑.md
│   └── 02-待讨论议题清单.md
└── 06-会议记录/
    └── 会议记录模板.md
```

---

## 建议讨论顺序

| 次序 | 文档 | 参与角色 | 目标产出 |
|------|------|----------|----------|
| 1 | `00-背景与目标` | 效率部、业务 Owner | 对齐「为什么要改、改什么、不改什么」 |
| 2 | `01-现状分析` | 产品、关键用户 | 确认痛点优先级 |
| 3 | `02-行业对标` | 产品、设计 | 对齐目标体验形态 |
| 4 | `03-新方案设计/*` | 产品、设计、研发 | **逐模块定方案** |
| 5 | `04-技术架构` | 架构、研发 | 可行性 & 集成边界 |
| 6 | `05-实施计划` | 全员 | Phase 1 MVP 范围签字 |

---

## 已达成共识（讨论前置）

以下结论来自前期差距分析，新方案 **默认继承**，讨论中如需推翻请显式标注：

1. **保留护城河**：Booking 自动接收、超排期审批、代发、预算硬控、IPD 活动级、PQA/PFC 链
2. **最大缺口**：从「空白 grid 填表」→「系统预填草稿 + 人工审核」
3. **不做**：桌面 activity 监控自动记工（合规风险）
4. **不降级**：不可收缩为飞书项目原生「工时登记插件」

---

## 文档维护

- 讨论结论写回对应 md 文件的 **「讨论结论」** 小节
- 每次评审后在 `06-会议记录/` 新增一条记录
- 定稿后可同步至飞书知识库
