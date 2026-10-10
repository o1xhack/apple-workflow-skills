import SwiftUI
struct Sample: View { let title: LocalizedStringResource = "Title"; var body: some View { LabeledContent { Text("Value") } label: { Text(title) } } }
