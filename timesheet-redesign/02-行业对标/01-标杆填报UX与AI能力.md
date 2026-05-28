# 标杆填报 UX 与 AI 能力

**目的：** 对齐「新填报页应该长什么样」的目标形态。

---

## 1. 五种行业 UI 范式

| 范式 | 代表产品 | 核心交互 | 适合 RIGOL？ |
|------|----------|----------|-------------|
| **A. 草稿确认页** | Timely AutoSheet、D365 Time Entry Agent | 系统预填 → 审核 → 一键提交 | ✅ **主推荐** |
| **B. Assist 弹窗** | Deltek Timesheet Assist | 登录弹推荐项目 → 加入 grid | ✅ 可作进页第一步 |
| **C. 日历时间轴** | Timewatch、Timely Timeline | 按时间块 drag 到项目 | ✅ 移动 + 会议场景 |
| **D. 卡片 My Work** | Tempo + Jira | 活动卡片一键记工 | 🟡 可参考，非主形态 |
| **E. Bot 对话** | SAP Joule、Deltek Teams | 自然语言补记 | 🟡 Phase 3 补充 |

---

## 2. 标杆 vs 我们现状

| 维度 | 标杆 | 我们现状 |
|------|------|----------|
| 默认首页 | 草稿列表 | 空白/满 grid |
| 行来源 | 自动 | 手选 |
| 小时来源 | 日历/Booking/历史 | 手填 |
| 备注 | 自动带会议名/WBS | 手写 |
| 提交 | 确认草稿 | 填完提交 |

---

## 3. 明确不采纳

| 方案 | 原因 |
|------|------|
| Timely Memory / Everhour 桌面监控 | 隐私合规、与代发/Booking 逻辑冲突 |
| 纯飞书项目工时插件 | 能力降级，缺 Booking 治理链 |

---

## 4. RIGOL 目标形态（草案）

```
进页 → Assist/草稿首屏（80% 已填）
     → 微调（列表或可选 grid）
     → 提交
移动 → 时间轴 + 待确认块（非 grid）
```

详见：`03-新方案设计/01-填报体验新方案（草稿优先）.md`

---

## 5. 参考链接

- [Deltek Timesheet Assist](https://www.deltek.com/en/blog/deltek-vantagepoint-timesheet-assist)
- [Timely AutoSheet](https://www.timely.com/feature/autosheet/)
- [D365 Copilot Time Entry](https://learn.microsoft.com/en-us/dynamics365/project-operations/time/copilot-in-time-entry)
- [Tempo Automation](https://help.tempo.io/timesheets/latest/what-is-tempo-automation)

---

## 6. 讨论结论

| 日期 | 结论 | 决策人 |
|------|------|--------|
| | | |
