import Cocoa

let WorkflowObjectPasteboardType =
  NSPasteboard.PasteboardType(rawValue: "alfred.workflow.objects.pasteboard")

let workflowObjJsonStrOpt: String? =
  NSPasteboard
    .general
    .pasteboardItems?
    .filter({ $0.types.contains(WorkflowObjectPasteboardType) })
    .first?
    .string(forType: WorkflowObjectPasteboardType)

print(workflowObjJsonStrOpt ?? "{}")
